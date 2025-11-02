# license

standalone `LICENSE` file generator written in python

## installation

clone the repository (the `licenses/` folder must stay next to the script):

```bash
git clone https://github.com/dragsbruh/license
cd license
chmod +x license.py
```

(optional) make a symlink in your `/usr/bin/` directory

```sh
sudo ln -s $(pwd)/license.py /usr/bin/license
```

### shell completions

only fish completions are supported as of now

add this to your `config.fish`

```sh
license shell fish | source
```

## usage

```bash
Usage: license <license|subcommand>
Subcommands:
  list                list available licenses (one per line)
  help                show this help message
  read                print license to stdout
  shell <language>    print shell completions (`fish`)
  <license> [file]    save license file to `file` (default: LICENSE)
```

## licenses

licenses are sourced from [spdx/license-list-data](https://github.com/spdx/license-list-data)
and are in plaintext format.

[see available licenses](./licenses/)

## LICENSE

congrats on reaching the actual license section

this software is licensed under the `The MIT License (MIT)`, see more info in [LICENSE](./LICENSE)
