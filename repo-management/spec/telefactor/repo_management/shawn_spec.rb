# frozen_string_literal: true

require 'spec_helper'

RSpec.describe Telefactor::RepoManagement::Shawn do
  describe '.resources_to_repos' do
    subject(:repos) { described_class.resources_to_repos(resources) }

    let(:resources) do
      [
        { name: 'shawn-00', html_url: 'example.com/shawn-00' },
        { name: 'shawn-01', html_url: 'example.com/shawn-01' },
        { name: 'shawn-02', html_url: 'example.com/shawn-02' }
      ]
    end

    it 'returns ::Repo objects' do
      expect(repos).to all(be_a_kind_of(Telefactor::RepoManagement::Shawn::Repo))
    end

    it 'sets Repo#name' do
      expect(repos).to all(
        have_attributes(name: /shawn-\d+/)
      )
    end

    it 'sets Repo#phase' do
      aggregate_failures do
        (0..2).each do |phase|
          expect(repos[phase].phase).to eq phase
        end
      end
    end

    it 'sets Repo#role based on phase' do
      aggregate_failures do
        expect(repos[0].role).to eq 'gm'
        expect(repos[1].role).to eq 'examiner'
        expect(repos[2].role).to eq 'sourcerer'
      end
    end
  end
end
