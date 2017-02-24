# util
Generic Utilities

Add ./bin to $PATH (export PATH={install dir}/bin;$PATH)
Add ./lib to $PYTHONPATH (export PYTHONPATH={install dir}/lib;$PYTHONPATH)

./compress_content.py
--[ Compresses the current directory per file and applies a password to the archive
  | Usage: ./compress_content.py -f dpx -p password

./findings.py
--[ Scans a directory tree and reports back the latest files which have been modified and when.
  | Usage: ./findings.py + (hard coded path at the top of script)

./icon_assign.py
--[ Bulk applies an icon to a file under Mac OS X
  | Usage: ./icon_assign.py file icon.png
  |        find . -type f -exec ./icon_assign.py {} icon.png \; (will set the same icon to all files in the current folder and onward)

./inpsector.py
--[ Simple python callback trace
  | Usage: copy/paste this into your code and observe.

./measure.py
--[ Simple profiler which reveals the performance differences between two code sets.
  | Usage: Self explanitory within the code.

[y mas][...]