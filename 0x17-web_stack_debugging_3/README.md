## 0x15. WEB STACK DEBUGGING #3

ENVIRONMENT
All files are written and compiles on Ubuntu 14.04 LTS. The first line of bash scripts will be exactly #!/usr/bin/env bash. Scripts are checked for style using Shellcheck version 0.3.3-1~ubuntu14.04.1`

### Requirements
>General
 - All your files will be interpreted on Ubuntu 14.04 LTS
 - All your files should end with a new line
 - A README.md file at the root of the folder of the project is mandatory
 - Your Puppet manifests must pass puppet-lint without any errors (version >= 1.1.0):
 - Your Puppet manifests must run without error
 - Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
 - Your Puppet manifests files must end with the extension .pp
 - Files will be checked with Puppet v3.4

### OBJECTIVE
> Use strace to find out why Apache returns a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing)
