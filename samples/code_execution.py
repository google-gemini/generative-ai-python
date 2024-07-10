# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from absl.testing import absltest

import google.generativeai as genai


class UnitTests(absltest.TestCase):
    def test_code_execution_basic(self):
        # [START code_execution_basic]
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools="code_execution")
        response = model.generate_content(
            (
                "What is the sum of the first 50 prime numbers? "
                "Generate and run code for the calculation, and make sure you get all 50."
            )
        )
        print(response.text)
        # [END code_execution_basic]
        # [START code_execution_basic_return]
        # ``` python
        # def is_prime(n):
        #     """
        #     Checks if a number is prime.
        #     """
        #     if n <= 1:
        #         return False
        #     for i in range(2, int(n**0.5) + 1):
        #         if n % i == 0:
        #             return False
        #     return True
        #
        # primes = []
        # num = 2
        # count = 0
        # while count < 50:
        #     if is_prime(num):
        #         primes.append(num)
        #         count += 1
        #     num += 1
        #
        # print(f'The first 50 prime numbers are: {primes}')
        # print(f'The sum of the first 50 prime numbers is: {sum(primes)}')
        #
        # ```
        # ```
        # The first 50 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
        # The sum of the first 50 prime numbers is: 5117
        #
        # ```
        # The code generated a list of the first 50 prime numbers, then sums the list to find the answer.
        #
        # The sum of the first 50 prime numbers is **5117**.
        # [END code_execution_basic_return]

    def test_code_execution_request_override(self):
        # [START code_execution_request_override]
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content(
            (
                "What is the sum of the first 50 prime numbers? "
                "Generate and run code for the calculation, and make sure you get all 50."
            ),
            tools="code_execution",
        )
        print(response.text)
        # [END code_execution_request_override]
        # [START code_execution_request_override_return]
        # ``` python
        # def is_prime(n):
        #     """
        #     Checks if a number is prime.
        #     """
        #     if n <= 1:
        #         return False
        #     for i in range(2, int(n**0.5) + 1):
        #         if n % i == 0:
        #             return False
        #     return True
        #
        # primes = []
        # num = 2
        # count = 0
        # while count < 50:
        #     if is_prime(num):
        #         primes.append(num)
        #         count += 1
        #     num += 1
        #
        # print(f'The first 50 prime numbers are: {primes}')
        # print(f'The sum of the first 50 prime numbers is: {sum(primes)}')
        #
        # ```
        # ```
        # The first 50 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
        # The sum of the first 50 prime numbers is: 5117
        #
        # ```
        # The code generated a list of the first 50 prime numbers, then sums the list to find the answer.
        #
        # The sum of the first 50 prime numbers is **5117**.
        # [END code_execution_request_override_return]

    def test_code_execution_chat(self):
        # [START code_execution_chat]
        model = genai.GenerativeModel(model_name="gemini-1.5-pro", tools="code_execution")
        chat = model.start_chat()
        response = chat.send_message(
            (
                "What is the sum of the first 50 prime numbers? "
                "Generate and run code for the calculation, and make sure you get all 50."
            )
        )
        print(response.text)
        # [END code_execution_chat]
        # [START code_execution_chat_return]
        # ``` python
        # def is_prime(n):
        #     """
        #     Checks if a number is prime.
        #     """
        #     if n <= 1:
        #         return False
        #     for i in range(2, int(n**0.5) + 1):
        #         if n % i == 0:
        #             return False
        #     return True
        #
        # primes = []
        # num = 2
        # count = 0
        # while count < 50:
        #     if is_prime(num):
        #         primes.append(num)
        #         count += 1
        #     num += 1
        #
        # print(f'The first 50 prime numbers are: {primes}')
        # print(f'The sum of the first 50 prime numbers is: {sum(primes)}')
        #
        # ```
        # ```
        # The first 50 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
        # The sum of the first 50 prime numbers is: 5117
        #
        # ```
        # The code generated a list of the first 50 prime numbers, then sums the list to find the answer.
        #
        # The sum of the first 50 prime numbers is **5117**.
        # [END code_execution_chat_return]


if __name__ == "__main__":
    absltest.main()
