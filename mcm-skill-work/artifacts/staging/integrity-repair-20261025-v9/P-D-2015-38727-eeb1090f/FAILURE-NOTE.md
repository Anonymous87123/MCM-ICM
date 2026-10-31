# Strict raw-generation equality check failed — retained

This attempt created only `recipe.py` and `fresh-native-full.bin`, then stopped before generating recovered views. The fresh text-only extraction came from the verified source PDF, but it differs in layout order and uses valid Unicode rather than the historical encoded-surrogate form.

The failed byte-equality check is not a visual or mathematical acceptance result. A later comparison must keep the two generations distinct, verify source witnesses on each, and never claim that recovering the old surrogate pairs proves complete equivalence to the fresh extraction. No live file was changed and this attempt is not overwritten.
