# Switch Game Deal Hunter 
 This repository contains a web scraper that gets Switch game prices from eBay to present the user with the best deals. THe goal of this project is to teach myself much of the data engineering fundamentals.  

- [x] write a scraper that goes on eBay and checks the prices that some product category sold for.
- [ ] Put the scraper in a docker container and host it inside gitlab container registry.
- [ ] spin up a Kubernetes cluster on a cloud service provider. 
- [ ] use helm to deploy airflow inside your kubernetes cluster
- [ ] write a dag and use airflow to instantiate your scraper, then scrape prices. You should set this scraper to run daily.
- [ ] store raw data from your scraper inside a Minio server running inside your kubernetes cluster
- [ ] use spark to read in the raw data from the Minio server, clean the data, and insert it into a Postgres database. (also running in your Kubernetes cluster)
- [ ] For extra points, write a stored procedure that calculate metrics on the pricing for the cards, (min, max, variance, rolling average, etc)
