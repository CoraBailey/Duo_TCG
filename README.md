# Card Renderer

A Python-based card rendering tool for generating customizable card images from structured data.

The project currently uses a personal trading card game prototype as its primary test case, but the long-term goal is to make the renderer flexible enough to support a wide variety of tabletop and card game projects without requiring users to adopt a specific card format.

## Current Features

* Generate card images from Python objects
* Render card names, descriptions, traits, statistics, and abilities
* Support multiple card attributes through reusable rendering methods
* Save generated cards automatically
* Archive older versions of cards when a new version is rendered
* Generate consistent filenames from card names
* Separate card data from rendering logic
* Support multiple card classes through a shared base structure

The current implementation is built using Python and Pillow.

## Project Structure

The project separates card definitions from the rendering system.

### Card Data

Card classes contain the information associated with a card, such as:

* Name
* Description
* Card type
* Attack
* Life
* Energy
* Capabilities
* Descriptors
* Distinctions
* Abilities

Different card types can extend a common base card structure and provide their own attributes.

### Renderer

The renderer is responsible for converting card data into an image.

Rendering functionality is divided into individual methods for elements such as:

* Card name
* Energy
* Traits
* Ability text
* Description
* Statistics

This structure is intended to make individual parts of the card layout easier to modify without rewriting the entire renderer.

### Version Archiving

When an existing card is rendered again, the previous image can automatically be moved into an archive directory before the new version is saved.

This makes it possible to iterate on card layouts and values while retaining earlier versions for comparison.

## Current Limitations

The renderer is still in an early development stage.

At the moment:

* Card layouts are primarily defined directly in Python
* Attribute placement is manually configured
* Fonts and visual styling have limited customization
* The renderer is currently tested primarily against one card game format
* Users cannot yet create templates through an external configuration
* Card data is currently created directly through Python objects
* There is not yet a graphical interface or standalone application

## Planned Features

The long-term goal is to move from a project-specific renderer toward a reusable card creation system.

### Custom Templates

Users will be able to define their own card layouts rather than relying on the current built-in format.

Templates may eventually define:

* Card dimensions
* Text regions
* Image regions
* Font sizes and styles
* Statistic placement
* Borders and backgrounds
* Attribute positioning
* Optional card elements

### Custom Attributes

Rather than requiring cards to use predefined fields such as Attack, Life, or Energy, users will be able to define their own attributes.

For example, one game might use:

* Attack
* Defense
* Mana

while another might use:

* Speed
* Influence
* Reputation
* Armor

The renderer should eventually treat these as configurable data rather than hard-coded fields.

### Reusable Game Formats

A user should eventually be able to create a template once and quickly generate many cards using the same format.

The intended workflow is roughly:

1. Create or select a card template.
2. Define the attributes used by the game.
3. Enter card data.
4. Apply the data to the template.
5. Generate the finished card image.

This would allow the renderer to support original tabletop games, prototypes, custom card sets, and other projects without requiring modification of the renderer itself.

### Data-Driven Card Creation

Future versions may support loading card data from external sources such as:

* JSON
* CSV
* YAML
* Databases

This would make it easier to manage larger card sets and generate many cards automatically.

### Template Configuration

Another planned goal is moving layout definitions away from hard-coded Python values.

Templates could potentially be stored as configuration files describing:

* Coordinates
* Dimensions
* Font settings
* Attribute names
* Alignment
* Visibility rules

This would make the rendering engine independent from any particular card game.

### User Interface

A future graphical interface could allow users to:

* Create templates visually
* Add or remove card attributes
* Adjust element positions
* Preview cards
* Select fonts and images
* Generate cards without editing Python code

## Project Goals

The main technical goal of this project is to create a flexible separation between:

**Card Data → Template → Renderer → Generated Image**

Rather than designing a renderer around one specific card game, the eventual system should allow the game format itself to be supplied by the user.

The current card game implementation serves as a practical environment for developing and testing these systems.

## Technologies

* Python
* Pillow
* Object-oriented card models
* File-based card versioning

Additional technologies may be introduced as the project expands.

## Status

This project is currently under active development and should be considered an early prototype.

The current focus is on improving the rendering system, expanding the information that can be displayed on cards, and gradually separating game-specific layout rules from the underlying renderer.


## Examples

Current example outputs generated by the renderer:

<p align="center">
  <img src="cards/examples/kara.png" width="300">
  <img src="cards/examples/lena.png" width="300">
  <img src="cards/examples/emma.png" width="300">
  <img src="cards/examples/regina.png" width="300">
</p>