# Trigger multi Jenkins job using API
## Usage 
### Get help
``` 
python main.py --help                                          
usage: main.py [-h] release_list_file job_type env_to_release

positional arguments:
  release_list_file  App list file to release
  job_type           PreparePromote or Promote
  env_to_release     Environment to release: release1/release2/staging
optional arguments:
  -h, --help         show this help message and exit
```
### Example
```
- To prepare release app to release1 env
    python main.py release_list PreparePromote release1
- To promote app to release1 env
    python main.py release_list Promote release1
```