# Getting started
To get started contributing to a textbook, first [install the CLI](#install-the-cli) and [clone an existing textbook](#clone-an-existing-textbook).
## Install the CLI
```
pip install openbook-textbook-engine
```
## Clone an existing textbook
Any textbook repository can be accessed from the Openbook site
1. On Openbook, go to Library and scroll down to the "All VCE" section
2. Click on the textbook you wish to contribute to
3. In the reader view, click on the export button in the top right. A modal will appear with a number of export options
4. Choose the option "Go to repository"
5. Clone the repository
## Create a new textbook
1. Run the command ```ote create [title]``` to create a textbook project in the working directory
2. Navigate to the project directory and edit options.json accordingly (example below)
```json
{
  "metadata": {
    "title": "Applied Computing Units 1 & 2",
    "authors": ["Richard Shelly"],
    "description": "Everything to know for Applied Computing Units 1 & 2"
  },
  "book": {
    "cover": {
      "cover-colour": "#FFE700"
    },
    "page_numbers": {
      "book/pre-content.md": "roman",
      "book/chapters": "numerical"
    }
  }
}
```
## Build the HTML output
Run the command ```ote build``` inside the **textbook directory**.
## Upload textbook
To submit a new textbook for approval on Openbook, first go to the Uploads Centre (this can be accessed from the sidebar as shown below).

https://github.com/user-attachments/assets/58bf5b9d-2a31-4d59-aa2e-a1aab096869b

Then, paste a link in the text field to a GitHub repository containing the textbook. Make sure you have configured a branch called 'release', because that's the one that Openbook looks for. Submit the textbook and then wait for an admin to either approve it or decline it.

