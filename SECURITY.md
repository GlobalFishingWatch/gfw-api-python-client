# Security

At **[Global Fishing Watch](https://globalfishingwatch.org/)**, we take the security of our users and the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) project very seriously. If you believe you have discovered a security vulnerability, we encourage you to report it responsibly. Please follow the process outlined below to ensure it is handled promptly and effectively.

## Reporting a Security Vulnerability

To protect our users and the project, please **do not** disclose security vulnerabilities publicly before they have been investigated and addressed. Here's how to report a security issue:

1.  **Do Not Open a Public Issue:** For the confidentiality of your report, please **do not** create a new issue on the public GitHub repository.

2.  **Contact the Global Fishing Watch APIs Team:** Please email the Global Fishing Watch APIs team directly, clearly marking your subject as a **Security Vulnerability Report**. You can find the email in the `authors` or `maintainers` section of the [`pyproject.toml`](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/pyproject.toml) file.

    **Subject:** Security Vulnerability Report - `gfw-api-python-client`

    In your email, please include as much detail as possible, such as:

    * A clear and concise description of the vulnerability.
    * The steps to reproduce the vulnerability (if applicable).
    * The potential impact of the vulnerability.
    * Any specific versions of `gfw-api-python-client` you believe are affected.
    * Your contact information so we can follow up with you.

3.  **Acknowledgement and Communication:** We will acknowledge receipt of your vulnerability report within **72 hours** and will make our best effort to provide you with regular updates on our investigation and remediation efforts through private communication.

## Vulnerability Handling Process

Once a security vulnerability is reported, we follow these steps:

1.  **Assessment:** The Global Fishing Watch APIs Team will promptly assess the reported vulnerability to understand its scope, severity, and potential impact.

2.  **Investigation:** We will thoroughly investigate the vulnerability, which may involve working with you for further clarification or reproduction steps.

3.  **Mitigation and Remediation:** Based on the assessment, we will develop and implement a plan to mitigate and remediate the vulnerability. This may involve patching the code, implementing workarounds, or providing specific guidance to users.

4.  **Disclosure (Coordinated):** Once the vulnerability has been fully addressed, we will coordinate with you on a public disclosure timeline. Our goal is to provide users with timely information about the vulnerability and the necessary steps to protect themselves. The disclosure will typically include:
    * A description of the vulnerability.
    * The affected versions of `gfw-api-python-client`.
    * The steps users need to take to upgrade or mitigate the issue.
    * Credit to the reporter (if they wish to be acknowledged).

## Security Updates

We are committed to regularly reviewing our codebase and dependencies for potential security weaknesses. Security fixes will be released as promptly as possible, typically in patch releases. We encourage users to stay informed about new releases and upgrade accordingly. Release notes will clearly indicate if a release contains security fixes.

## Security Best Practices for Users and Contributors

To help ensure the security of your applications and contributions to `gfw-api-python-client`, we recommend following these best practices:

* **Keep Your Dependencies Up-to-Date:** Regularly update `gfw-api-python-client` and all its dependencies to the latest stable versions to benefit from the latest security fixes.
* **Secure Credential Management:** Avoid hardcoding API access tokens or other sensitive credentials directly in your code. Utilize environment variables, secure configuration files, or dedicated secret management tools.
* **Dependency Auditing:** Regularly audit your project's dependencies for known security vulnerabilities using tools like `pip-audit` or integrated security scanning features in your development environment or CI/CD pipeline.
* **Follow Secure Coding Practices:** When contributing code, adhere to secure coding principles to minimize the introduction of new vulnerabilities. Be mindful of common security risks such as injection flaws, insecure data handling, and improper error handling.

We appreciate your efforts in helping us maintain a secure and reliable `gfw-api-python-client`. Your responsible reporting is crucial to the security of our community.
