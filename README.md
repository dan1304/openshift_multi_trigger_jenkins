# Trigger multi Jenkins job using API
### How it works 
```
- Define app list needs to release in the `release_list_file`
- Script maps the app release list with `dependencyDocs`
- Script triggers the pipelines directly in Jenkins with the data get from above steps
```
### Usage
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
    python main.py release_list_release1 PreparePromote release1
- To promote app to release1 env
    python main.py release_list_release1 Promote release1
```