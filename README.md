Ghidra ARM64 (AARCH64) Instruction Processor Manual Patch
=================
This things are code for generate idx file for ARM64(AARCH64) for [Ghidra](https://github.com/NationalSecurityAgency/ghidra).

Also this repo include modified ldefs and idx file that generated from me.

Install ldefs and idx
-----------------
### Resouce
* https://static.docs.arm.com/ddi0487/db/DDI0487D_b_armv8_arm.pdf
* modified\AARCH64.idx
* modified\AARCH64.ldefs

Create directory "__GhidraPath__\Ghidra\Processors\ARM\data\manuals"

Download [DDI0487D_b_armv8_arm.pdf](https://static.docs.arm.com/ddi0487/db/DDI0487D_b_armv8_arm.pdf)

Copy pdf and idx file to "__GhidraPath__\Ghidra\Processors\ARM\data\manuals".

Replace AARCH64.ldefs "__GhidraPath__\Ghidra\Processors\AARCH64\data\languages\AARCH64.ldefs"

done.

But if there's update on AARCH64.ldefs must be modify yourself.

idx genearte code
-----------------
It's very dirty now. 
Will fix later. If you want genrate own. fix "ARMv8a_man_path" var that pointing path of input pdf.

Issue
-----------------
Cannot catch instructions page in 
```
K13.2 Alphabetical index of AArch64 registers and System instructions
K13.4 Alphabetical index of AArch32 registers and System instructions
```
will fix soon.

for ```AArch64 registers and System instructions```

It seems in C5.3 to C5.5. it will easy to fix for adding them.
