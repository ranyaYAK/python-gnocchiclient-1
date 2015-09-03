#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from gnocchiclient.tests.functional import base


class ArchivePolicyRuleClientTest(base.ClientTestBase):
    def test_archive_policy_rule_scenario(self):
        # CREATE
        result = self.gnocchi(
            u'archivepolicyrule', params=u"create -a name:test"
                                         u" -a archive_policy_name:high"
                                         u" -a metric_pattern:disk.io.*")
        policy_rule = self.details_multiple(result)[0]
        self.assertEqual('test', policy_rule["name"])

        # GET
        result = self.gnocchi(
            'archivepolicyrule', params="show test")
        policy_rule = self.details_multiple(result)[0]
        self.assertEqual("test", policy_rule["name"])

        # DELETE
        result = self.gnocchi('archivepolicyrule',
                              params="delete test")
        self.assertEqual("", result)

        # GET FAIL
        result = self.gnocchi('archivepolicyrule',
                              params="show test",
                              fail_ok=True, merge_stderr=True)
        self.assertFirstLineStartsWith(result.split('\n'),
                                       "Not Found (HTTP 404)")

        # DELETE FAIL
        result = self.gnocchi('archivepolicyrule',
                              params="delete test",
                              fail_ok=True, merge_stderr=True)
        self.assertFirstLineStartsWith(result.split('\n'),
                                       "Not Found (HTTP 404)")