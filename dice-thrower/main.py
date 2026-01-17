i  c51c24c feat(config): add just (#68) (11 months ago)
                      872dcfa chore(build): auto-generate docs (1 year, 1 month ago)

                  ● which-key.nvim 1.23ms  VeryLazy
                      3aab214 chore(build): auto-generated vimdocs (3 months ago)
                      8c15e22 chore(update): update repository (#1020) (3 months ago)
                      b4177e3 chore(build): auto-generate docs (3 months ago)
                      f76f78e ci: update minit.lua (3 months ago)
                      5e2a0b7 ci: update test scripts (3 months ago)
                      904308e chore(build): auto-generate docs (4 months ago)
                      7ea0fe4 fix(view): double footer border. Fixes #964 (#974) (4 months ago)
                      370ec46 chore(build): auto-generate docs (11 months ago)


                Loaded (1)
                  ● noice.nvim 1.59ms  VeryLazy

                Not Loaded (4)
                  ○ conform.nvim  <leader>cF  <leader>cF (x)  ConformInfo
                  ○ incline.nvim  BufReadPre
                  ○ rustaceanvim  rust
                  ○ zen-mode.nvim  <leader>z  ZenMode

                Disabled (2)
                  ○ flash.nvim
                  ○ render-markdown.nvimmport random

def roll_dice():
    return random.randint(1, 6)

while True:
    print(f"The number of the dice is: {roll_dice()}")

    option = .input("Throw again? (y/n): ").lower()

    if option != "y":
        print("Game finished.")
        break

