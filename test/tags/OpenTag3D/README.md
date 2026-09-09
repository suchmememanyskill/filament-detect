# Polar Filament spool fixture

This is Polar Filament PLA Pure Light Blue, serial `50017-FYG5`, SKU `P023`,
OpenTag3D version 2.000. The `.payload.hex` file preserves the 216 payload bytes
supplied from the physical tag. The capture omits the final eight zero bytes of
the 224-byte memory-map range, exercising the spec's missing-byte rule.

The `.bin` file wraps those captured bytes in a generated MIME NDEF record and
Type 2 TLV, with a simulated capability container and zero-filled system-memory
prefix, then pads the image to 540 bytes for the existing fixture test suite.
Only the payload is captured; framing and surrounding memory are generated.
Tests supply a dummy UID and verify the binary contains the exact payload.

The `.yml` file specifies expected GenericFilament output. The `.decoded.yml`
file checks all decoded fields, including fields that are not exported.
Expected values are independent of the runtime decoder. Edge-case tests modify
copies of the payload; those modifications do not describe this spool.
