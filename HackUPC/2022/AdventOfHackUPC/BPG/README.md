## Exploit: Broken page

### Description
### This one will introduce you a bit to Docker because you will need to run a docker in order to find the solution.

cat exploit-challenge.tar.gz.a? > exploit-challenge.tar.gz

sudo docker image load < exploit-challenge.tar.gz
sudo docker run -p 8000:8000 adventofhackupc/exploit-challenge:latest

Then open http://localhost:8000/ on your pc. 
