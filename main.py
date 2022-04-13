from releaseUtils import releaseDetails, jenkinsApiTrigger
import argparse
def getReleaseList(list_to_release):
    release_list = []
    with open(list_to_release, 'r') as f:
        for line in f:
            app = line.split()
            release_list.append(app)
    return release_list

if __name__ == '''__main__''':
    '''
    python main.py app_release_list.txt job_type environment 
    '''
    # get args from command line input
    parser = argparse.ArgumentParser()
    parser.add_argument("release_list_file", help="App list file to release")
    parser.add_argument("job_type", help="PreparePromote or Promote")
    parser.add_argument("env_to_release", help="Environment to release: release1/release2/staging")
    args = parser.parse_args()
    list_to_release = args.release_list_file
    job_type = args.job_type
    env_to_release =  args.env_to_release
    # print(list_to_release)
    # print(env_to_release)
    # print(job_type)
    # print(job_type=="PreparePromote")

    
    # trigger jenkins job 
    release_list = getReleaseList(f'./{list_to_release}')
    for app_name in release_list:
        app_name = app_name[0]
        print(app_name)
        new_release_details = releaseDetails(app_name).getReleaseDetails()
        app_version = new_release_details[1]
        new_job = jenkinsApiTrigger(app_name, app_version, env_to_release)
        if job_type == "PreparePromote":
            trigger_new_job = new_job.preparePromote()
            print(trigger_new_job)
        elif job_type == "Promote":
            trigger_new_job = new_job.promote()
            print(trigger_new_job)
        else: 
            print("Run with --help for details")

