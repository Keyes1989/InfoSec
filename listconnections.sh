#!/bin/bash
lsof -i | grep -E "(LISTEN|ESTABLISHED)"
