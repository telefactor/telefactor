
## Testing basic cyclic relationship
```

Added person: amoeba
Added amoeba as parents of amoeba

```
## final file
```json

{
  "people": [
    {
      "name": "amoeba"
    }
  ],
  "relationships": [
    {
      "child_name": "amoeba",
      "parent_name": "amoeba"
    }
  ]
}
```
## Trying to get grandparent
```

bundler: failed to load command: fam (~/.rvm/gems/ruby-2.6.1/bin/fam)
ArgumentError: comparison of String with 0 failed
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family/relationship_list.rb:46:in `>='
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family/relationship_list.rb:46:in `get_grandparent_names'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family.rb:93:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam.rb:106:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/cli/get.rb:98:in `call'
  ~/.rvm/gems/ruby-2.6.1/gems/hanami-cli-0.3.1/lib/hanami/cli.rb:57:in `call'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/cli.rb:20:in `call'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/exe/fam:10:in `<top (required)>'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `load'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `<top (required)>'

```
## Trying to get gpt 10
```

bundler: failed to load command: fam (~/.rvm/gems/ruby-2.6.1/bin/fam)
ArgumentError: comparison of String with 0 failed
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family/relationship_list.rb:46:in `>='
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family/relationship_list.rb:46:in `get_grandparent_names'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family.rb:93:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam.rb:106:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/cli/get.rb:98:in `call'
  ~/.rvm/gems/ruby-2.6.1/gems/hanami-cli-0.3.1/lib/hanami/cli.rb:57:in `call'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/cli.rb:20:in `call'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/exe/fam:10:in `<top (required)>'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `load'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `<top (required)>'

```
## Trying to get gpt 10,000
```

bundler: failed to load command: fam (~/.rvm/gems/ruby-2.6.1/bin/fam)
ArgumentError: comparison of String with 0 failed
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family/relationship_list.rb:46:in `>='
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family/relationship_list.rb:46:in `get_grandparent_names'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/family.rb:93:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam.rb:106:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/cli/get.rb:98:in `call'
  ~/.rvm/gems/ruby-2.6.1/gems/hanami-cli-0.3.1/lib/hanami/cli.rb:57:in `call'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/lib/fam/cli.rb:20:in `call'
  ~/workspace/telefactor-root/telefactor-fam-examiner-one/exe/fam:10:in `<top (required)>'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `load'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `<top (required)>'

```

