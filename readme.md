# TCD Time Table Fetcher

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Selenium](https://img.shields.io/badge/Selenium-3.141.0-blue)](https://pypi.org/project/selenium/)
[![Python](https://img.shields.io/badge/Python-3.8.8-blue)](https://www.python.org/)

## About this Project
This project is a simple web scraper that fetches the timetable for a given student from the TCD Timetable website. It is currently in the development stage and is not yet ready for use.

## Technologies Used
- Python
- Selenium
- BeautifulSoup

Currently the cookies are retrieved with selenium. However, this is not ideal as it requires a browser to be opened. In the future, I plan to use the BeautifulSoup library to fetch the cookies.

## To Do
- [ ] Fetch the timetable.
- [ ] Fetch the cookies using BeautifulSoup.
- [ ] Add a GUI. (PyQt5)
- [ ] Add a feature to save the timetable to a file.
- [ ] Save the timetable to a database.
- [ ] Fetch any additional classes that students aren't enrolled in but want to take.
- [ ] Export the timetable to a calendar file.

## How to Use

**Code has not yet reached a stage where it can be used.**

## Configuration
The configuration file is located at `config/config.json`. The configuration file contains the following fields:
- `username`: The username of the student.
- `password`: The password of the student.

Sample:
```json
{
    "username": "username",
    "password": "password"
}
```

## License
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.