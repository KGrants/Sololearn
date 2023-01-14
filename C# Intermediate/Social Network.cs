using System;
using System.Collections.Generic;

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            string postText = Console.ReadLine();

            Post post = new Post();
            post.Text = postText;
            post.ShowPost();

        }
    }

    class Post
    {
        private string text;
        
        public string Text
        {
            get {return text;}
            set {text = "New post\n"+value;}
        }

        public void ShowPost()
        {
            Console.WriteLine(text);
        }
        
        //write a property for member text
        
    }
}