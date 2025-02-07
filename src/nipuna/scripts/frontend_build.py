import subprocess
import os
import sys

def build_frontend():

    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    frontend_path = os.path.join(package_dir, 'ui')
    os.chdir(frontend_path)

    dist_path = os.path.join(frontend_path, 'dist')
    node_modules_path = os.path.join(frontend_path, 'node_modules')

    if not os.path.exists(dist_path) or not os.path.exists(node_modules_path):
        
        try:
            subprocess.run(['npm', 'i',"--silent"])
            subprocess.run(['npm', 'run', 'build'])
        except subprocess.CalledProcessError as e:
            print(f"Error building frontend: {e}")
            sys.exit(1)
    else:
        pass