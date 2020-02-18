# frozen_string_literal: true

require 'spec_helper'

RSpec.describe Telefactor::RepoManagement::Fam do
  describe '.resources_to_repos' do
    subject(:repos) { described_class.resources_to_repos(resources) }
    let(:resources) do
      [
        {
          name: 'telefactor-fam-examiner-1', html_url: 'example.com/telefactor'
        }
      ]
    end

    it 'returns ::Repo objects' do
      expect(repos).to all(be_a_kind_of(Telefactor::RepoManagement::Fam::Repo))
    end
  end
end
