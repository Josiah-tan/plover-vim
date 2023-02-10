# 0.10.0

adjustments to number system:
removed zero numbers from 4-9 (too much overhead)
changed KR → K for dollar
added num2word W → to convert number to word

# 0.9.0

switching from `-TSZ` to `-LTSZ` for command object
added `#EU` register for miscellaneous
switched to `-B` → ```, `#-B` → `q`, because `@` → `FP` and `q` → `#FP` (idea of playback verses making)
switching from `-TDZ` to `-TSZ` for command object
added plover-vim tutor

# 0.8.0

these commands moved from command_object (old) → miscellaneous (new):
-FB (change surround)
#-FB (change surround)
#-FP → #-F (surround)

moved several commands from command object to miscellaneous
The command object system is designed with middles in mind, if these aren't used, then they should be placed in miscellaneous instead, to save space...

fixed test suite (was broken in 0.7)

# 0.7.1

I literally can't code, forgot to add spaces between gl and gL... Sigh

# 0.7.0 

videos will be coming soon!
added support for the lion plugin (gl and gL)
lion is `-PB` and `#-PB`
lion commands are to be two stroked! (two stroking commands with numbers are not supported yet in plover-vim-extended e.g. `vip3gl,`, but will come soon after I get used to plover-vim-extended first)
Zen is now `-FPB` instead of `-PB` (sorry for shuffling that around, but I guess it makes sense for Zen to be `-FPB`)
recording macros are now `#-FP` instead of `-FPB`, it makes sense for the recording and using macros to have the same base stroke in my opinion!


# 0.6.1

added support for other systems other than english stenotype
-from plover.system import english_stenotype as e
+import plover.system as e


# 0.6.0

added official support for marks, unimpaired, repeat (miscellaneous category)

# 0.5.0

Added {plover:clear_trans_state} as default state
this means that output → start attached is required (to ensure that attachment works)

handles edge cases where:

`hello world <escape>Fw ciw world {:uppercase_everything}` → `hello WORLD WORLD`

# 0.4.0

plover-vim mostly finished

number theory still needs to be finalized
