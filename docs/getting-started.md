# Getting started
To get started contributing to a textbook, first [install the CLI](#install-the-cli) and [clone an existing textbook](#clone-an-existing-textbook). Then, refer to the [Authors' guide]().
## Install the CLI
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
      "style": "standard",
      "theme": "yellow"
    },
    "page_numbers": {
      "book/pre-content.md": "roman",
      "book/chapters": "numerical"
    }
  }
}
```