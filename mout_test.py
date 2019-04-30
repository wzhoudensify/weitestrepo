import os
import subprocess

def main():
        if os.path.exists('/root/.virtualenv/my_env'):
            print('existed')
        else:
            subprocess.run(['/bin/sh', 'create_env.sh'])
            print('created haha')


if __name__ == "__main__":
    main()
