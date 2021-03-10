Ghidra ARM64 (AARCH64) Instruction Processor Manual Patch
=================
This things are code for generate idx file for ARM64(AARCH64) for [Ghidra](https://github.com/NationalSecurityAgency/ghidra).

Also this repo include modified ldefs and idx file that generated from me.

### Story telling about this repo with Korea Description.
[해당 마크다운 문서](<./etc/Story of Pulling request to NSA Ghidra.md>)

Install ldefs and idx
-----------------
### Resouce
* https://static.docs.arm.com/ddi0487/ea/DDI0487E_a_armv8_arm.pdf (it was updated at July 05 2019)
* modified\AARCH64.idx
* modified\AARCH64.ldefs

Create directory "__GhidraPath__\Ghidra\Processors\AARCH64\data\manuals"

Download [DDI0487E_a_armv8_arm.pdf]https://static.docs.arm.com/ddi0487/ea/DDI0487E_a_armv8_arm.pdf)

Copy pdf and idx file to "__GhidraPath__\Ghidra\Processors\AARCH64\data\manuals".

Replace AARCH64.ldefs "__GhidraPath__\Ghidra\Processors\AARCH64\data\languages\AARCH64.ldefs"

done.

But if there's update on AARCH64.ldefs must be modify yourself.

idx genearte code
-----------------
It's very dirty now. 
Will fix later. If you want genrate own. fix "ARMv8a_man_path" var that pointing path of input pdf.

Resolved Issue
-----------------
```
K13.2 Alphabetical index of AArch64 registers and System instructions
    C5.3 A64 System instructions for cache maintenance
    C5.4 A64 System instructions for address translation
    C5.5 A64 System instructions for TLB maintenance
```

Remove this things
```
D9.2 Alphabetical list of Statistical Profiling Extension packets
F5.1 Alphabetical list of T32 and A32 base instruction set instructions
```

TODO
-----------------
### A32 System instructions in TRM. And coudn't decide for adding them.
```
K13.4 Alphabetical index of AArch32 registers and System instructions
```
Exactly they are AARCH32 instruction that working in AARCH64. I cannot sure should I add them for current ghidra system.
Currently I removed but not sure this is right behavior.

### SIMD , NEON , Normal , A32, or other version's instructions were mixed but meesed up or not matching to Ghidra.
A32 and A64 version of "add" are mixed and they have same index but page number in my idx file. I will fix this.

And there's several version for SIMD and NEON , anything others were mixed. I should check ghidra's name tagging and my tagging are same together.

