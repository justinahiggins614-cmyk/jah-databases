import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave11-universal-engine"))
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code"))
import engine
if __name__ == "__main__":
    engine.build_slug('gen-infinite-comparison-engine')
