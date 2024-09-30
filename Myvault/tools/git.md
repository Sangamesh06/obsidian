to clone pr authored by others use the below command
git fetch upstream pull/{{pr_number}}/head:pr_{{pr_number}}_{{client_dir_name}}

from now on to clone company clone
use command
git clone git@github.com-company:sangamesh-somashetti-unbxd/solution-jobs-v2.git


and personal
git clone git@github.com-personal:your-username/your-personal-repo.git




for using diffrent ssh key for already local repo
You’re correct in understanding that using `ssh-add` to add different SSH keys to the SSH agent will affect which key is used for authentication. Here’s how it works in your scenarios:

### Key Usage with `ssh-add`

1. **When Adding a Key:**
    - **For Company Repository:**
```
ssh-add ~/.ssh/id_rsa

```

        
        This command adds your company's SSH key to the SSH agent. Any operations (like pushing) in repositories configured to use this key will use it for authentication.
        
    - **For Personal Repository:**
```
ssh-add ~/.ssh/id_ed25519_personal2

```

        
        This command adds your personal SSH key to the SSH agent. Any operations in repositories configured to use this key will use it for authentication.
        

### Key Management

1. **Persistent Key Addition:**
    
    - **SSH Agent Session:** When you run `ssh-add`, the key is added to the SSH agent for the current terminal session. If you close the terminal or restart your computer, you’ll need to re-add the keys.
        
    - **Persistent Across Sessions:** To keep the keys available across terminal sessions, you can configure your SSH agent to automatically load the keys when you log in. For macOS, you can do this by adding the keys to the SSH agent in your shell profile file (e.g., `.bash_profile`, `.zshrc`):
        

```
# Add to ~/.bash_profile or ~/.zshrc
eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_rsa
ssh-add -K ~/.ssh/id_ed25519_personal
```

        
        The `-K` flag (or `--apple-use-keychain` in newer versions) ensures that your keys are added to the macOS keychain for persistence.
        
2. **Switching Between Projects:**
    
    - If you switch between projects in an IDE, the SSH agent will use the currently loaded key(s) for authentication, depending on which key is active.
    - If you need to use different keys, ensure the appropriate key is loaded with `ssh-add`. You can list currently loaded keys with:
 
```
ssh-add -l

```

    - If you need to switch keys, you can remove the currently loaded key(s) and add the required ones:

```
ssh-add -d ~/.ssh/id_rsa   # Remove company key
ssh-add ~/.ssh/id_ed25519_personal2  # Add personal key

```
        

### Summary

- **Add keys with `ssh-add`** to use them for the current terminal session.
- **Configure automatic loading** of keys in your shell profile for persistence across sessions.
- **Switch keys as needed** based on the repository you’re working with, especially if switching between company and personal projects.

By managing your keys in this way, you can ensure that the correct key is used for authentication based on the repository you’re working with.