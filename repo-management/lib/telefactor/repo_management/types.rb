# frozen_string_literal: true

require 'dry-struct'

module Telefactor::RepoManagement
  module Types
    include Dry.Types

    module Custom
      class StrictStruct < Dry::Struct
        # throw an error when unknown keys provided
        schema schema.strict
        # convert string keys to symbols
        transform_keys(&:to_sym)

        def to_s
          "#<#{self.class.name} #{
            self.class.schema.keys.map { |key|
              "#{key.name}=#{self[key.name].inspect}"
            }.join(' ')
          }>"
        end
      end
    end
  end
end
