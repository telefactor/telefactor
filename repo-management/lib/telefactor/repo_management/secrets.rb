# frozen_string_literal: true

require 'dry-struct'
require 'safe_yaml'

SafeYAML::OPTIONS[:default_mode] = :safe

module Telefactor::RepoManagement
  module Secrets
    class << self
      def secrets
        @secrets ||= wrap_with_models(load_yaml_file)
      end

      def load_yaml_file
        SafeYAML.load_file('./config/secrets.yaml')
      end

      def wrap_with_models(secrets_hashes)
        Models::Secrets.new(secrets_hashes)
      end
    end

    module Models
      Types = Dry.Types

      class BaseModel < Dry::Struct
        # throw an error when unknown keys provided
        schema schema.strict
        # convert string keys to symbols
        transform_keys(&:to_sym)
      end

      class GitHub < BaseModel
        attribute :access_token, Types::String
      end

      class Secrets < BaseModel
        attribute :github, GitHub
      end
    end
  end
end
