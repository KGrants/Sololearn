using System;
using System.Collections.Generic;

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            Draw pencil = new Draw();
            Draw brush = new Brush();
            Draw spray = new Spray();

            pencil.StartDraw();
            brush.StartDraw();
            spray.StartDraw();

        }
    }

    public interface IDraw
    {
        void StartDraw();
    }

    class Draw : IDraw
    {
        public virtual void StartDraw()
        {
            Console.WriteLine("Using pencil");
        }
    }
    
    class Brush:Draw
    {
        public override void StartDraw()
        {
            Console.WriteLine("Using brush");
        }
    }

    class Spray:Draw
    {
        public override void StartDraw()
        {
            Console.WriteLine("Using spray");
        }

    }
}