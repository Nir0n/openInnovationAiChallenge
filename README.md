# Open Innovation Ai Challenge
## Cloud test
Demo with AWS instance: http://54.208.252.93:5000/api/get_image_frames?depth_min=9000&depth_max=9002
## Local test 
1) ```git clone https://github.com/Nir0n/openInnovationAiChallenge.git```
2) ```cd openInnovationAiChallenge```
3) ```docker-compose build```
4) ```docker-compose up```
5) first you need to run in terminal ```curl -X POST http://54.208.252.93:5000/api/start-processing/img.csv``` to populate db
6) now you can test with http://54.208.252.93:5000/api/get_image_frames?depth_min=9000&depth_max=9002
## Possible impovements
1) add reverse proxy
2) cqrs pattern for segregation read and writes
3) with 2 option add required repositories
