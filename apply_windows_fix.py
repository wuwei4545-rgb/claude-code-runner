#!/usr/bin/env python3
"""
Apply Windows path compatibility fixes to src/container.ts
"""
import re

def apply_fixes():
    with open('src/container.ts', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: Replace the first tarFile definition and add tempDirPath creation
    content = re.sub(
        r"(\s+// Create tar archive using git archive for tracked files \+ untracked files\n\s+)const tarFile = `/tmp/claude-runner-\$\{Date\.now\(\)\}\.tar`;",
        r"""// Create temporary directory early (relative path approach for Windows compatibility)
		const tempDirPath = path.join(workDir, '.claude-runner-tmp');
		if (!fs.existsSync(tempDirPath)) {
			fs.mkdirSync(tempDirPath, { recursive: true });
		}

		// Create tar archive using git archive for tracked files + untracked files
		// Use relative path for git/tar commands to avoid Windows path issues
		const tarFileRel = `.claude-runner-tmp/claude-runner-${Date.now()}.tar`;
		const tarFile = path.join(workDir, tarFileRel);""",
        content
    )
    
    # Fix 2: Update git archive command to use relative path
    content = re.sub(
        r'execSync\(`git archive --format=tar -o "\$\{tarFile\}" HEAD`',
        'execSync(`git archive --format=tar -o "${tarFileRel}" HEAD`',
        content
    )
    
    # Fix 3: Update tar command for tracked files
    content = re.sub(
        r'const fileListPath = `/tmp/claude-runner-tracked-\$\{Date\.now\(\)\}\.txt`;',
        'const fileListPath = path.join(tempDirPath, `claude-runner-tracked-${Date.now()}.txt`);',
        content
    )
    
    # Fix 4: Update tar -cf command with relative path
    content = re.sub(
        r'execSync\(`tar -cf "\$\{tarFile\}" --files-from="\$\{fileListPath\}"`',
        'execSync(`tar -cf "${tarFileRel}" --files-from="${path.basename(fileListPath)}"`',
        content
    )
    
    # Fix 5: Update tar -cf command for empty archive
    content = re.sub(
        r'execSync\(`tar -cf "\$\{tarFile\}" -T /dev/null`',
        'execSync(`tar -cf "${tarFileRel}" -T /dev/null`',
        content
    )
    
    # Fix 6: Update untracked files path
    content = re.sub(
        r'const fileListPath = `/tmp/claude-runner-files-\$\{Date\.now\(\)\}\.txt`;',
        'const fileListPath = path.join(tempDirPath, `claude-runner-files-${Date.now()}.txt`);',
        content
    )
    
    # Fix 7: Update tar -rf command
    content = re.sub(
        r'execSync\(`tar -rf "\$\{tarFile\}" --files-from="\$\{fileListPath\}"`',
        'execSync(`tar -rf "${tarFileRel}" --files-from="${path.basename(fileListPath)}"`',
        content
    )
    
    # Fix 8: Update git tar file definition
    content = re.sub(
        r'const gitTarFile = `/tmp/claude-runner-git-\$\{Date\.now\(\)\}\.tar`;',
        r"""const gitTarFileRel = `.claude-runner-tmp/claude-runner-git-${Date.now()}.tar`;
		const gitTarFile = path.join(workDir, gitTarFileRel);""",
        content
    )
    
    # Fix 9: Update tar command for git
    content = re.sub(
        r'execSync\(\s*`tar -cf "\$\{gitTarFile\}" --exclude="._\*" --exclude=".DS_Store" \$\{combinedFlags\} \.git`',
        'execSync(\n\t\t\t`tar -cf "${gitTarFileRel}" --exclude="._*" --exclude=".DS_Store" ${combinedFlags} .git`',
        content
    )
    
    # Fix 10: Update other /tmp paths in _copyClaudeConfig
    content = re.sub(
        r'const tarFile = `/tmp/claude-json-\$\{Date\.now\(\)\}\.tar`;',
        r"""const tarFileRel = `.claude-runner-tmp/claude-json-${Date.now()}.tar`;
			const tarFile = path.join(tempDirPath, tarFileRel);""",
        content
    )
    
    # Fix 11: Update other /tmp paths for directory copy
    content = re.sub(
        r'const tarFile = `/tmp/claude-dir-\$\{Date\.now\(\)\}\.tar`;',
        r"""const tarFileRel = `.claude-runner-tmp/claude-dir-${Date.now()}.tar`;
			const tarFile = path.join(tempDirPath, tarFileRel);""",
        content
    )
    
    # Fix 12: Update git config  tar file
    content = re.sub(
        r'const tarFile = `/tmp/git-config-\$\{Date\.now\(\)\}\.tar`;',
        r"""const tarFileRel = `.claude-runner-tmp/git-config-${Date.now()}.tar`;
		const tarFile = path.join(tempDirPath, tarFileRel);""",
        content
    )
    
    with open('src/container.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Applied Windows compatibility fixes to src/container.ts")

if __name__ == '__main__':
    apply_fixes()
