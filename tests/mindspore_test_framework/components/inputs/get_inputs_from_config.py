# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Component that return raw inputs."""

from ...components.icomponent import IDataComponent

class IdentityDC(IDataComponent):
    """
    Return inputs.

    Examples:
        'inputs': [
            np.array([[2, 2], [2, 2]]).astype(np.float32)
        ]
    """
    def create_inputs(self, verification_set):
        return verification_set['inputs']