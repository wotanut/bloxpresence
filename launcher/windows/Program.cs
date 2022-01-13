using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace inheritance
{
    class Program
    {
        static void Main(string[] args)
        {
            Process launch = new Process();

            launch.StartInfo.UseShellExecute = false;
            launch.StartInfo.FileName = "../bloxpresence/setup.py";
            launch.StartInfo.CreateNoWindow = true;
            launch.Start();
        }
    }
}