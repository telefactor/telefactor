
## Testing basic cyclic relationship
```

Added person: amoeba
Added amoeba as parents of amoeba

```
## final file
```json

{
  "amoeba": [
    "amoeba"
  ]
}
```
## Trying to get grandparent
```

bundler: failed to load command: fam (~/.rvm/gems/ruby-2.6.1/bin/fam)
RuntimeError: Parent 'amoeba' not found for 'amoeba'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:29:in `block in find_parent'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:28:in `tap'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:28:in `find_parent'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:21:in `block in create_person'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:20:in `map'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:20:in `create_person'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:9:in `block in deserialize'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:8:in `reverse_each'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:8:in `deserialize'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:80:in `load_from_file'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:72:in `using_tree'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:64:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/cli/get.rb:74:in `call'
  ~/.rvm/gems/ruby-2.6.1/gems/hanami-cli-0.3.1/lib/hanami/cli.rb:57:in `call'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/cli.rb:20:in `call'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/exe/fam:10:in `<top (required)>'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `load'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `<top (required)>'

```
## Trying to get gpt 10
```

bundler: failed to load command: fam (~/.rvm/gems/ruby-2.6.1/bin/fam)
RuntimeError: Parent 'amoeba' not found for 'amoeba'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:29:in `block in find_parent'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:28:in `tap'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:28:in `find_parent'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:21:in `block in create_person'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:20:in `map'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:20:in `create_person'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:9:in `block in deserialize'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:8:in `reverse_each'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:8:in `deserialize'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:80:in `load_from_file'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:72:in `using_tree'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:64:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/cli/get.rb:74:in `call'
  ~/.rvm/gems/ruby-2.6.1/gems/hanami-cli-0.3.1/lib/hanami/cli.rb:57:in `call'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/cli.rb:20:in `call'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/exe/fam:10:in `<top (required)>'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `load'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `<top (required)>'

```
## Trying to get gpt 10,000
```

bundler: failed to load command: fam (~/.rvm/gems/ruby-2.6.1/bin/fam)
RuntimeError: Parent 'amoeba' not found for 'amoeba'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:29:in `block in find_parent'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:28:in `tap'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:28:in `find_parent'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:21:in `block in create_person'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:20:in `map'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:20:in `create_person'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:9:in `block in deserialize'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:8:in `reverse_each'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/family/serialization/family_deserializer.rb:8:in `deserialize'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:80:in `load_from_file'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:72:in `using_tree'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam.rb:64:in `get_grandparents'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/cli/get.rb:74:in `call'
  ~/.rvm/gems/ruby-2.6.1/gems/hanami-cli-0.3.1/lib/hanami/cli.rb:57:in `call'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/lib/fam/cli.rb:20:in `call'
  ~/workspace/telefactor-root/telefactor-fam-sourcerer-three/exe/fam:10:in `<top (required)>'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `load'
  ~/.rvm/gems/ruby-2.6.1/bin/fam:23:in `<top (required)>'

```

