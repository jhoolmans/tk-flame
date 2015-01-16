# Copyright (c) 2014 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.
#
#
# This script is a launch wrapper for Flame. It is part of the flame bootstrap.
# The flame bootstrap happens in three distinct steps:
#
# 1. Preparation - The multi-launch-app (for example) executes the 
#    python/startup/bootstrap.py method (after having imported this file.
#    This method takes the launch parameters (executable to run, parameters etc).
#    And returns a re-written set of executables, so that instead of launching 
#    the DCC (which is what the launch-app is wanting to do) the bootstrap modifies
#    this and returns the executable to run being this app_launcher script with 
#    the executable as the command line. It also adjusts certain things that strictly 
#    need to be defined before any flame related process is launched - on our case
#    instructions to the dynamic loader via LD_LIBRARY_PATH
#
# 2. The launch app will now call *this* script rather than the DCC which it was configured
#    to launch. This script executes with /usr/discreet/Python-2.6.9/bin/python which is a known
#    environment with pyside etc. At this point, we start the engine and run a bunch of startup
#    stuff. Note that this is now happening before flame has actually launched. This startup
#    includes ensuring that a new project exists. It also sets up the flame envrironment variables,
#    so that flame can run the right hooks once it has been launched. The last step of this script 
#    is to actually launch flame.
#
# 3. Flame launches, user performs operations. Engine hooks (in the /flame_hooks folder) are executed.
#


import os
import sys

try:
    import sgtk
    from sgtk import TankError    
except ImportError:
    raise Exception("Could not find the sgtk library in the PYTHONPATH")


def launch_flame(dcc_path, dcc_args):
    """
    Run pre-processes and eventually launch flame.
    
    This process is executing inside a flame python environment where
    pyside is guaranteed to exist. It is also assumed that sgtk is already 
    available in the pythonpath, as it would typically be if executed via the 
    multi launch app for example. 
    
    :param dcc_path: Path to the flame dcc executable or start script
    :param dcc_args: Args to pass to dcc

    :returns: 0 on success, non-zero on failure
    """
    # pick up environment
    engine_instance_name = os.environ["TOOLKIT_ENGINE_NAME"]
    context_str = os.environ["TOOLKIT_CONTEXT"]
    context = sgtk.context.deserialize(context_str)
    
    # start up flame engine
    # set a special environment variable to help hint to the engine
    # that when it is started this time, it is part of the bootstrap
    # and happening *outside* of the actual flame DCC
    os.environ["TK_FLAME_ENGINE_MODE"] = "PRE_LAUNCH"
    flame_engine = sgtk.platform.start_engine(engine_instance_name, context.sgtk, context)
    del os.environ["TK_FLAME_ENGINE_MODE"]
    
    app_args = flame_engine.bootstrap()

    # now launch flame!
    flame_engine.log_debug("-" * 60)
    flame_engine.log_debug("About to launch the actual flame DCC.")
    flame_engine.log_debug("Dcc      path: '%s'" % dcc_path)
    flame_engine.log_debug("App      args: '%s'" % app_args)
    flame_engine.log_debug("External args: '%s'" % dcc_args)
    cmd_line = "%s %s %s &" % (dcc_path, app_args, " ".join(dcc_args))
    flame_engine.log_debug("Full command line '%s'" % cmd_line)
    flame_engine.log_debug("-" * 60)
    
    return os.system(cmd_line)
    


if __name__ == "__main__":

    # the first argument is always the path to the flame executable
    if len(sys.argv) == 1:
        logger.error("Invalid syntax: app_launcher /path/to/flame args!")
        sys.exit(1)
        
    # the location of the actual tank core installation
    dcc_path = sys.argv[1]
    
    # rest of the arguments are stuff we should pass to the DCC
    dcc_args = sys.argv[2:]

    exit_code = 1
    try:
        exit_code = launch_flame(dcc_path, dcc_args)
    except KeyboardInterrupt, e:
        print "Process cancelled."


    sys.exit(exit_code)