import * as vscode from 'vscode';
import axios, { AxiosInstance } from 'axios';

interface DeepSeekConfig {
    serverUrl: string;
    autoComplete: boolean;
    temperature: number;
    maxTokens: number;
}

class DeepSeekClient {
    private client: AxiosInstance;
    private config: DeepSeekConfig;

    constructor(config: DeepSeekConfig) {
        this.config = config;
        this.client = axios.create({
            baseURL: config.serverUrl,
            timeout: 120000,
        });
    }

    async complete(prompt: string): Promise<string> {
        try {
            const response = await this.client.post('/api/complete', {
                prompt,
                max_tokens: this.config.maxTokens,
                temperature: this.config.temperature,
            });
            return response.data.completion;
        } catch (error) {
            throw new Error(`Completion failed: ${error}`);
        }
    }

    async reviewCode(code: string, language: string): Promise<string> {
        try {
            const response = await this.client.post('/api/review', {
                code,
                language,
            });
            return response.data.review;
        } catch (error) {
            throw new Error(`Code review failed: ${error}`);
        }
    }

    async health(): Promise<boolean> {
        try {
            const response = await this.client.get('/health');
            return response.data.status === 'healthy';
        } catch (error) {
            return false;
        }
    }

    async listModels(): Promise<any> {
        try {
            const response = await this.client.get('/api/models');
            return response.data;
        } catch (error) {
            throw new Error(`Failed to list models: ${error}`);
        }
    }

    async loadModel(modelName: string): Promise<any> {
        try {
            const response = await this.client.post('/api/models/load', {
                model_name: modelName
            });
            return response.data;
        } catch (error) {
            throw new Error(`Failed to load model: ${error}`);
        }
    }

    async getModelStatus(): Promise<any> {
        try {
            const response = await this.client.get('/health');
            return response.data;
        } catch (error) {
            throw new Error(`Failed to get model status: ${error}`);
        }
    }
}

class DeepSeekCopilot {
    private client: DeepSeekClient | null = null;
    private statusBar: vscode.StatusBarItem;
    private outputChannel: vscode.OutputChannel;
    private currentModel: string | null = null;

    constructor() {
        this.statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
        this.outputChannel = vscode.window.createOutputChannel('DeepSeek Copilot');
    }

    async initialize(context: vscode.ExtensionContext) {
        const config = this.loadConfig();
        this.client = new DeepSeekClient(config);

        // Register commands
        this.registerCommands(context);

        // Check server health
        await this.checkServerHealth();

        // Update status bar
        this.updateStatusBar();

        // Show welcome message
        this.outputChannel.appendLine('🚀 DeepSeek Copilot initialized!');
    }

    private loadConfig(): DeepSeekConfig {
        const config = vscode.workspace.getConfiguration('deepseek-copilot');
        return {
            serverUrl: config.get('serverUrl') || 'http://localhost:8000',
            autoComplete: config.get('autoComplete') ?? true,
            temperature: config.get('temperature') ?? 0.7,
            maxTokens: config.get('maxTokens') ?? 256,
        };
    }

    private registerCommands(context: vscode.ExtensionContext) {
        context.subscriptions.push(
            vscode.commands.registerCommand('deepseek-copilot.complete', () => this.handleComplete()),
            vscode.commands.registerCommand('deepseek-copilot.review', () => this.handleReview()),
            vscode.commands.registerCommand('deepseek-copilot.startServer', () => this.handleStartServer()),
            vscode.commands.registerCommand('deepseek-copilot.stopServer', () => this.handleStopServer()),
            vscode.commands.registerCommand('deepseek-copilot.listModels', () => this.handleListModels()),
            vscode.commands.registerCommand('deepseek-copilot.switchModel', () => this.handleSwitchModel()),
            vscode.commands.registerCommand('deepseek-copilot.modelStatus', () => this.handleModelStatus()),
            vscode.commands.registerCommand('deepseek-copilot.configure', () => this.handleConfigure())
        );
    }

    private async handleComplete() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active editor');
            return;
        }

        if (!this.client) {
            vscode.window.showErrorMessage('DeepSeek client not initialized');
            return;
        }

        const selection = editor.selection;
        const text = editor.document.getText(new vscode.Range(0, 0, selection.start.line, selection.start.character));

        try {
            await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Notification,
                    title: 'DeepSeek: Generating completion...',
                    cancellable: false,
                },
                async () => {
                    const completion = await this.client!.complete(text);
                    editor.edit((editBuilder) => {
                        editBuilder.insert(selection.end, completion);
                    });
                    this.outputChannel.appendLine(`✅ Completion: ${completion.substring(0, 100)}...`);
                }
            );
        } catch (error) {
            vscode.window.showErrorMessage(`Completion failed: ${error}`);
            this.outputChannel.appendLine(`❌ Error: ${error}`);
        }
    }

    private async handleReview() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active editor');
            return;
        }

        if (!this.client) {
            vscode.window.showErrorMessage('DeepSeek client not initialized');
            return;
        }

        const code = editor.document.getText();
        const language = editor.document.languageId;

        try {
            await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Notification,
                    title: 'DeepSeek: Reviewing code...',
                    cancellable: false,
                },
                async () => {
                    const review = await this.client!.reviewCode(code, language);
                    this.outputChannel.appendLine('\n📋 Code Review:');
                    this.outputChannel.appendLine(review);
                    this.outputChannel.show();
                }
            );
        } catch (error) {
            vscode.window.showErrorMessage(`Review failed: ${error}`);
            this.outputChannel.appendLine(`❌ Error: ${error}`);
        }
    }

    private async handleStartServer() {
        vscode.window.showInformationMessage('To start the backend server, run: python backend/main.py');
        this.outputChannel.appendLine('ℹ️  Start backend with: cd backend && python -m uvicorn main:app --reload');
    }

    private async handleStopServer() {
        vscode.window.showInformationMessage('Stop the backend server manually (Ctrl+C in terminal)');
    }

    private async handleListModels() {
        if (!this.client) {
            vscode.window.showErrorMessage('DeepSeek client not initialized');
            return;
        }

        try {
            const data = await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Window,
                    title: 'DeepSeek: Fetching available models...',
                    cancellable: false,
                },
                async () => await this.client!.listModels()
            );

            const items: vscode.QuickPickItem[] = [];
            if (data.suggested_models) {
                items.push(...data.suggested_models.map((model: any) => ({
                    label: model.name,
                    detail: model.description,
                    description: model.size,
                })));
            }

            const selected = await vscode.window.showQuickPick(items, {
                placeHolder: `Current model: ${data.current_model}`,
                canPickMany: false,
            });

            if (selected) {
                const confirmation = await vscode.window.showInformationMessage(
                    `Load model ${selected.label}?`,
                    'Yes',
                    'No'
                );
                if (confirmation === 'Yes') {
                    await this.handleSwitchModel(selected.label);
                }
            }
        } catch (error) {
            vscode.window.showErrorMessage(`Failed to list models: ${error}`);
        }
    }

    private async handleSwitchModel(modelName?: string) {
        if (!this.client) {
            vscode.window.showErrorMessage('DeepSeek client not initialized');
            return;
        }

        let targetModel = modelName;
        if (!targetModel) {
            const input = await vscode.window.showInputBox({
                prompt: 'Enter Hugging Face model ID to load',
                placeHolder: 'e.g. gpt2 or meta-llama/Llama-2-7b-hf',
            });
            if (!input) {
                return;
            }
            targetModel = input.trim();
        }

        try {
            await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Notification,
                    title: `DeepSeek: Loading model ${targetModel}...`,
                    cancellable: false,
                },
                async () => await this.client!.loadModel(targetModel!)
            );

            vscode.window.showInformationMessage(`Loaded model: ${targetModel}`);
            this.currentModel = targetModel;
            this.updateStatusBar();
        } catch (error) {
            vscode.window.showErrorMessage(`Failed to load model: ${error}`);
        }
    }

    private async handleModelStatus() {
        if (!this.client) {
            vscode.window.showErrorMessage('DeepSeek client not initialized');
            return;
        }

        try {
            const info = await this.client.getModelStatus();
            vscode.window.showInformationMessage(
                `Model: ${info.model} | Device: ${info.device} | 8-bit: ${info['8bit_enabled'] ? 'Enabled' : 'Disabled'}`
            );
            this.currentModel = info.model;
            this.updateStatusBar();
        } catch (error) {
            vscode.window.showErrorMessage(`Failed to read model status: ${error}`);
        }
    }

    private async handleConfigure() {
        vscode.commands.executeCommand('workbench.action.openSettings', 'deepseek-copilot');
    }

    private async checkServerHealth() {
        if (!this.client) return;

        try {
            const info = await this.client.getModelStatus();
            this.currentModel = info.model;
            this.outputChannel.appendLine('✅ DeepSeek backend server is running');
            this.updateStatusBar();
        } catch (error) {
            this.outputChannel.appendLine('⚠️  DeepSeek backend server is not responding');
            vscode.window.showWarningMessage(
                'DeepSeek backend server not found. Make sure it\'s running on http://localhost:8000',
                'Start Server'
            );
            this.statusBar.text = '$(debug-disconnect) DeepSeek';
            this.statusBar.tooltip = 'DeepSeek Copilot - backend not running';
            this.statusBar.show();
        }
    }

    private updateStatusBar() {
        this.statusBar.text = `$(sparkle) DeepSeek ${this.currentModel ? `(${this.currentModel})` : ''}`;
        this.statusBar.tooltip = `DeepSeek Copilot - Model: ${this.currentModel || 'Unknown'}`;
        this.statusBar.show();
    }
}

let copilot: DeepSeekCopilot;

export function activate(context: vscode.ExtensionContext) {
    console.log('🚀 Activating DeepSeek Copilot extension...');
    copilot = new DeepSeekCopilot();
    copilot.initialize(context);
}

export function deactivate() {
    console.log('❌ DeepSeek Copilot deactivated');
}
