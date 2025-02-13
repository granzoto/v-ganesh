#!/usr/bin/env python3

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import random
from flask import Flask
from flask import url_for

app = Flask(__name__)

ganeshisms = [
    "We're doomed.",
    "I foresee nothing but failure in the future.",
    "My dog is my best friend even though she despises me.",
    "I cannot go camping because I will be eaten by a bear.",
    "It's Elon's fault.",
    "You make me sad.",
    "I am cold.",
    """I'm going to buy a new car.</p><p>New cars are too expensive.</p><p>I'm
    going to drive my old car until it explodes.""",
    "If you retire I'm going to be in trouble.",
    """I need to learn A.I.</p>
    <p>There's a ton of jobs in A.I.</p>
    <p>It's too late for me to learn A.I.""",
    """I'm going to move to Mexico.</p><p>We can live like kings in Mexico.""",
    """Can you stay on after the meeting?</p><p>I have a question.""",
    "That's not very nice, Ken.",
    "We are going to be millionaires !!"
]

@app.route("/")
def hello_world():
    random.seed();
    gman_url = url_for('static', filename='headshot.jpg')
    template = f'<p><center><img src="{gman_url}" alt="Virtual Ganesh" class="center"></center></p>'
    template += f'<center><big><p>{random.choice(ganeshisms)}</p></big></center>'
    return template
