
require 'dry-struct'

module Telefactor::RepoManagement
  module Types
    include Dry.Types()

    module Custom
      class StrictStruct < Dry::Struct
        # throw an error when unknown keys provided
        schema schema.strict
        # convert string keys to symbols
        transform_keys(&:to_sym)
      end
    end
  end
end

