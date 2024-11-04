 Data Processing Scripts
 This repository contains scripts for processing data from various sources, including extracting phone numbers,
 URLs, and validating email addresses. Below is a brief overview of each functionality: ###
 1. Phone Number Extraction
 2.  The script reads a dataset from a CSV file (`User_DATA.txt`) containing phone numbers. It cleans the data by removing any leading or trailing whitespace and uses
 a regular expression to extract phone numbers in various formats, including those with country codes. The extracted phone numbers are stored in 
 a new column for easy access.
 **Example of the Regex Pattern Used:** ```regex (\+\d{1,3}\s?\(?\d{1,3}\)?[\s-]?\d{3}[\s-]?\d{4}|\d{3}[-]\d{3}[-]\d{4})
 ``` This pattern matches phone numbers formatted with or without country codes and various delimiters
. ### 2. URL Extraction
 The script extracts URLs from a predefined text block. It utilizes a regular expression to identify and capture URLs that start with either `http` or `https`. The extracted URLs
 are stored in a DataFrame, which makes it easy to work with them for further analysis or processing.
 **Example of the Regex Pattern Used:**
```regex https?://[^\s]+
``` This pattern captures any URL beginning with `http://` or `https://`, followed by any characters until a whitespace
 is encountered.
 ### 3. Email Validation
 The script validates email addresses from a DataFrame by applying a regex pattern that checks for valid email
formats. It filters out invalid email addresses and retains only those that meet the specified criteria, which includes the presence of valid characters
 and specific domain extensions (such as `.com` or `.co`).
**Example of the Regex Pattern Used:
** ```regex [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co) ```
 This pattern matches email addresses that contain valid characters before the `@` symbol and require the domain to end with `.com` or `.co`.
 ### Conclusion
 These scripts are designed to facilitate data cleaning and extraction tasks, making it easier to work with phone numbers, URLs, and email addresses.
 For further customization or additional features, feel free to modify the regex patterns or the underlying logic.
