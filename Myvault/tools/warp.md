

whenever we use / stating at file path it means the path is from root folder
whenver you want tot ccopy an entire folder from one place to other use cp -r instead of just cp


enter cmd + I to enter agent mode


/Users/unbxd/downloads/Visual Studio Code 2.app/contents/resources/app/bin


export PATH="$PATH:/downloads/Visual Studio Code 2.app/contents/resources/app/bin"

command to move all screenshots into a ingle folder
```
mv ~/Desktop/*.png  ~/Desktop/scst/
```

just replace png with whatever file type  you want to move name of folder so that a they all move into one folder

###  1 .Command Search & Autocomplete

- Warp offers smart autocomplete with contextual suggestions. This helps speed up command entry and reduces the need to remember exact command syntax.
- You can use **`Ctrl + R`** to search through your command history, allowing you to quickly find and reuse previous commands.

### 2. **Blocks and Command Outputs**:

- Warp separates your commands and their outputs into **blocks**, making it easier to read and manage terminal sessions. You can collapse, expand, and even copy specific blocks for better organization.
- Use **`Cmd + K`** to clear the terminal without losing block history.

### 3. **Workflows**:

- Warp allows you to save common sequences of commands as **workflows**. You can create, share, and reuse these workflows to automate tasks. This is great for repetitive tasks like deployments, testing, or setting up environments.

### 4. **Split Panes & Tabs**:

- Use split panes and multiple tabs to work with different environments or tasks side by side. This can be especially useful for monitoring logs, running tests, or managing different server connections.
- Shortcut: **`Cmd + D`** (split horizontally) and **`Cmd + Shift + D`** (split vertically).

### 5. **Custom Themes and Keybindings**:

- Warp supports customizable themes and keybindings. You can tailor the terminal's look and feel to your preferences, which can improve focus and efficiency.
- Check out the settings with **`Cmd + ,`** to explore theme options.

### 6. **Shell Integration**:

- Warp supports multiple shell types like **Bash, Zsh, and Fish**. Use this to your advantage by integrating your preferred shell configuration files (like `.bashrc` or `.zshrc`) for personalized aliases, environment variables, and prompt setups.

### 7. **AI Command Suggestions**:

- Warp's AI can suggest command corrections and completions based on the context. This reduces the chances of errors and helps with less frequently used commands.

### 8. **SSH & Remote Development**:

- Warp works well with SSH connections for remote development. It offers performance improvements over traditional terminals, especially when dealing with large outputs.

### 9. **Collaborative Sessions**:

- You can share terminal sessions with team members in real time. This is helpful for debugging, pair programming, or live collaboration in complex environments.

### 10. **Command Palette**:

- Access the **command palette** with **`Cmd + P`** to quickly find any command, workflow, or configuration option within Warp.

By leveraging these features, you can improve your productivity and streamline your development workflow with Warp.


check for cpu usage 
top(command) will show appliccation aloong with resource usage 
to exit the same simply type q



alias 1='open -a warp'
alias 2='open -a "CopyClip"'
alias 3='open -a "Google chrome"'
alias 4='open -a "Rectangle.app"'
alias 5='open -a "obsidian"'
alias 6='open -a "PyCharm CE"'
open -a 'finder