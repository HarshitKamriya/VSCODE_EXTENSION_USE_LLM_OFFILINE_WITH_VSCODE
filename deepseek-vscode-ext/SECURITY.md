# Security Policy

## Reporting a Security Vulnerability

If you discover a security vulnerability in the DeepSeek VS Code Integration, please email security@deepseek.com instead of using the issue tracker. Please include:

1. Description of the vulnerability
2. Steps to reproduce
3. Potential impact
4. Suggested fix (if available)

We take security seriously and will respond promptly.

## Security Considerations

### Local Processing
- All code processing happens locally on your machine
- No data is sent to external servers
- No cloud dependencies

### Model Integrity
- Models are downloaded from official Hugging Face repositories
- Verify model checksums before use
- Keep models updated for security patches

### API Security
- Backend server binds to localhost by default
- Change host/port in .env for network access
- Always validate user input in prompts
- Use environment variables for sensitive config

### Data Privacy
- Code suggestions are not stored
- No analytics or telemetry
- Complete privacy control

## Best Practices

1. **Keep Dependencies Updated**
   ```bash
   pip install --upgrade -r requirements.txt
   npm update
   ```

2. **Use Virtual Environments**
   - Always use Python venv or similar
   - Isolate project dependencies

3. **Secure Configuration**
   - Never commit .env files
   - Use .env.example as template
   - Restrict file permissions: `chmod 600 .env`

4. **Network Security**
   - Default: localhost only
   - If exposing to network:
     - Use firewall rules
     - Consider authentication
     - Use HTTPS proxy

## Known Issues

None currently reported. Please report any security concerns promptly.

## Supported Versions

| Version | Status | Security Updates |
|---------|--------|------------------|
| 0.1.x   | Alpha  | Yes              |
| < 0.1   | EOL    | No               |

## Security Checklist

- [ ] Running on trusted machine
- [ ] Python environment isolated (venv)
- [ ] .env file not committed to version control
- [ ] Backend only accessible from localhost
- [ ] Dependencies kept up to date
- [ ] Model checksums verified
- [ ] Code review before deployment

---

For more details, see README.md and INSTALLATION.md
