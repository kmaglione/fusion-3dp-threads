This repository contains a set of Fusion 360 thread definitions for ISO metric
threads with adjustible tolerances, for use with 3D printing. They are inspired
by, but in no way derived from, [this project][replicant-3dp-threads].

# Usage

Once installed, each ISO Metric Profile thread size additional thread classes,
for tolerances between ±.1mm and ±.9mm, as long as threads with those tolerances
would actually mesh with an opposing thread with standard tolerances:

![Thread size selection](screenshots/edit_hole.png)

These tolerances indicate the amount of additional space added between opposing
surfaces, be they the the opposing thread profiles, or the opposing major/minor
diameter. You should typically choose a tolerance to match the tolerance of your
printer. For instance, if you are printing a vertical screw hole and your
printer has 200 micron horizontal tolerance, you should start with ±.2mm
tolerance and adjust from there.

As an example, below on the left, we have an M5 hole with ±.2mm clearance and a
screw with standard clearance, compared with an M5 hole and screw both with
standard clearance on the right:

![M5+.2mm](screenshots/M5+.2mm.png)
![M5](screenshots/M5.png)

The opposing thread profiles are .2mm further apart, and the major and minor
diameters are .2mm larger. The pitch diameter, however, is .4mm larger, and the
additional backlash is approximately .46mm.

Given the 60° angle of ISO metric profile threads, the difference in pitch
diameter and additional backlash relative to standard tolerance are as follows:

| Tolerance   | Pitch Delta | Backlash |
| ----------- | ----------- | -------- |
| `0.1`       | `0.2`       | `0.23`   |
| `0.2`       | `0.4`       | `0.46`   |
| `0.3`       | `0.6`       | `0.69`   |
| `0.4`       | `0.8`       | `0.92`   |
| `0.5`       | `1.0`       | `1.15`   |
| `0.6`       | `1.2`       | `1.39`   |
| `0.7`       | `1.4`       | `1.62`   |
| `0.8`       | `1.6`       | `1.85`   |
| `0.9`       | `1.8`       | `2.08`   |

# Installation

The `adjust_threads.py` script generates a new set of thread definitons based on
the stock Fusion 360 `ISOMetricprofile.xml` thread definitions file:

```
python adjust_threads.py ISOMetricprofile.xml >ISOMetricTolerances.xml
```

To use the definitions, they must be installed into Fusion 360's thread
definition directory for your user account. You may simply overwrite the
existing `ISOMetricprofile.xml` file, or create a new file with any arbitrary
name you choose.

For Windows, the thread definitions are stored in:

```
%LocalAppData%\Autodesk\webdeploy\Production\<version ID>\Fusion\Server\Fusion\Configuration\ThreadData
```

and for MacOS, they are stored in:

```
~/Library/Application Support/Autodesk/Webdeploy/production/<version ID>/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData
```

where `<version ID>` is a hash value specific to each Fusion 360 version. You
will typically want the folder with the most recent modification date, and you
will need to re-install in the appropriate folder for the current version after
each update unless you use the [ThreadKeeper][threadkeeper] add-on.

[replicant-3dp-threads]: https://replicantfx.com/custom-threads-with-fusion-360/

[threadkeeper]: https://apps.autodesk.com/FUSION/en/Detail/Index?id=1725038115223093226
