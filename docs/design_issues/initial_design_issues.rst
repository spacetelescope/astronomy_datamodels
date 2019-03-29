Various Issues
==============

This is an initial list of open issues regarding the prototype data models. Many of the decisions that were made are fairly arbitrary and a broader consensus on final choices is needed.

General categories:
===================

General Principle adopted
-------------------------

There are two major choices I made along these lines with major implications:

1) Keeping data collections flat. Rather than arbitrary nesting of groups of data (e.g., by detector for an instrument, by exposures, by visits, by proposals, etc) a flat structure seems much more preferable. The idea is to provide tools to select groups of the data more flexibly. Currently this is done using string keys, where the string is a combination of multiple field values using a specified field separator (user/software specifiable). A list could be used, but then that requires more complex means of digging out attributes for grouping purposes. It would be preferable to have tools to construct the keys that way according to the needed usage. So here the flat structure is a dictionary, the keys are a combination of field values, presumably obtained from attributes of the observations.

Note that this structure, although designated MOS, is fairly general to any set of data with fairly homogeneous characteristics. E.g., Image sets could be handled the same way (with either the images as part of the ASDF file or just references to other data files).

2) A large part defining these is to encourage the development of standard approaches to storing calibrated data meaning standard organizations of attributes, standard attributes, and standard meanings of attributes. These should be shaken out by actual use and practice, and along those lines we should start with minimal choices to allow additional standards to be grown. To that end almost all of the objects listed below allow a standard meta attribute. While the objects also allow additional attributes beyonds the properties defined, using that should be discouraged since we cannot guarantee that a consensus will develop for an attribute name that will conflict with what some users have chosen. So the encouraged practice should be to put all nonstandard metadata and data objects within the meta attribute (which is always a dictionary). In that way futher standardization will not collide with user additions.

3) (more minor) Where there is a possibility of more than one value of an attribute, I always use a list (array), even if there is only one. I figure that getting people used to thinking that way simplifies the code with regard to lots of conditional checking. For items that benefit from names, a dictionary is used instead (e.g., for WCS)

Can the model code be more automated?
-------------------------------------

It sure seems like much of the tag and object code could be generated from the schema. That hasn't been done to keep things straightforward, but it may be something to consider in the future. Editor macros sure were useful for this, particularly for the property code

Is the directory structure for the schemas suitable?
----------------------------------------------------

I'm not entirely happy with the differences between the schema tree (which will be relocated to a different repository using git submodule when things stabilize). The schema path uses singular astronomy_datamodel and datamodel and the code uses the plural for astronomy_datamodels. In any case the scheme paths probably should be reworked.

Are the names chosen for objects suitable?
------------------------------------------

As a summary there are the object names currently defined (from top down)

meta is an attribute of all of these (perhaps with a couple exceptions)

**Mos** (multiple object spectra)
- fields [r] (dict of name [r], data attribute path, type [string or int])
- field_separator [r] (how to split key string into fields)
- datasets [r] (dict of Spectrum instances)
**Spectrum** (eventually should also support external data references)
- sci [r] (Quantity instance)
- dq (numpy array)
- err (Quantity instance)
- wcs [r] (WcsSet instance)
- aperture (SpectrumAperture instance)
- background_corrected (boolean)
- background_apertures (list of aperture ids)
- obsinfo (ObsContext instance; preferably all the attributes of that are attributes of Spectrum, but that isn't working yet)

**ObsContext** (all attributes are optional)
- telescope (Telescope instance)
- instrument (Instrument instance)
- proposal (Proposal instance)
- observers (list of Observer instances)
- target (Target instance)
- associated_data (dict)

**SpectrumAperture** (definition of aperture shape in the slit plane)
- center [r] (in slit plane, presumably in the same system that the GWCS defines)
- footprint [r] (array of vertices)
- aperture_id [r] string or int

**WcsSet** (a dict of GWCS objects; the "default" key and value are required)

**Target**
- id [r]
- coordinates (astropy coord object) [r]
- name
- aliases

**Telescope**
- name [r]
- organization
- org_url
- telescope_url
- telescope_type
- location_name
- location (Location instance, Fixed or Moving) [r]

**FixedLocation** (on a solar system body, longitude, latitude, etc)
- solar_system_body [r] defaults to Earth
- latitude (Angle quantity) [r]
- longitude  (ditto)
- altitude (quantity)

**MovingLocation** (not done yet, e.g., spacecraft)

**Instrument**
- name [r]
- instrument_type [r]
- filters (as a list) [r]
- disperser
- spectral_range
- mode
- detectors (Detector instances in a list) [probably should only allow one value...]
- engineering (dict of enginering info)

**Detector2dCCD** (I had anticipated a IR version, but so far, I don't have any particular differences in attributes to standardize for calibrated data; suggestions?)
- name [r]
- size (x, y) [r]
- binning (x, y)
- subarray Subarray instance

**Subarray** (defining a subset of the full detector)
- size (x,y) [r]
- offset (x,y) [r]
- name
**Proposal**
- id [r]
- title
- proposers [list of observers]
**Observer**
- name [r]
- institution
- address
- email address
- isPI


Is the code structure suitable?
-------------------------------

Currently every data model object has its own source file, both for tags and the intrinisc objects. This leads to smaller files, but with the use of properties, they aren't that small.

Type checking:
--------------

Currently properties are used to check that the objects are suitably initialized and that the types correspond to what the schema expects (I think this is preferable since getting schema error messages is generally less transparent).

Unit Tests:
-----------

Currently there is at least one per schema, but these are fairly minimal since reworking all these if changes are made will take time. Best to get some buy-in first.

Work needed for ASDF:
---------------------

- Automatic pointer detection: As we generate files that refer to multiple data items, many of these may share common objects (particularly WCS) and duplicating such is wasteful. It should be possible to only store these once.

- An easy way of writing large ASDF file without requiring storing all data in memory when writing out. It may be possible now, but good examples of how to do this are needed.