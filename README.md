# DataHub
http://www.tokencrates.com/

A webs server that is capable of storing publicly available data into a database and returning the resources to authorized users through REST API. The server will built with Flask framework and the front-end will be designed using libraries such as Bootstrap. 

The data will either be downloaeded in csv format or pulled with API requests and inserted into the database via Spark script. Each type of data will be mapped to a common format so users will be able to easily access the data from different sources. 

The server will be running on a virtual private server with a monolithic architecture.

## Use case

Any user who is interested in using data for analytical, research, or business purposes will be able to look up open source data throughout the web. It will have detailed instructions so a beginner can come and learn how to access those data from the server. 

## Functionalities

1. Register/Login
2. View user info
3. Settings
4. Map data into a common format
5. Allow API requests

## Available Data

US Census Data (https://www.census.gov/data/datasets/2010/dec/demographic-profile-with-geos.html)

## Getting Started

### API Documentation  
Census data:  
Name: /api/cnesus/name/  
ID: /api/census/id/ 

### Example API Request: 

/api/census/name/san%20francisco%20city  
```
{  
  "census": [  
    {  
      "country": "US",   
      "county": null,   
      "countycc": null,  
      "division": 9,  
      "geocomp": "00",  
      "housing_unit": 376942,  
      "id": 6345,  
      "latitude": 37.7272391,  
      "longitude": -123.0322294,  
      "name": "San Francisco city",  
      "place": 67000,  
      "population": 805235,  
      "region": 4,  
      "state": 6  
    }  
  ]  
}  
```
## Built With

* [Flask] (http://flask.pocoo.org/) - Web framework
* [Bootstrap] (https://getbootstrap.com/) - Front-end framework
* [PostgreSQL] (https://www.postgresql.org/) - Database
* [Spark] (https://spark.apache.org/) - Big Data Tool

## Contributing

## Versioning

## Authors

* **Tae Hyon Lee** - (https://github.com/leeth7830)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
