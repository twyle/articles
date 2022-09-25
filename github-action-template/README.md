# github-action-template
A template for creating GitHub Actions.

## Inputs

## `myinput`

**Required** The users name. Default `"world"`.

## Outputs

## `myoutput`

A greeting with the users name i.e hello world

## Example usage

```

- name: github action template
  id: selftest
  uses: lyleokoth/github-action-template@v0.2.2
  with:
    myinput: Lyle

- name: action output
  run: |
    echo "${{ steps.selftest.outputs.myoutput }}
```
