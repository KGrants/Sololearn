using System; 
using System.Collections.Generic;

namespace Code_Coach_Challange
{
	class Program
	{
		public static void Main(string[] args)
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
            set {text = value;}
        }
		
		public void ShowPost()
		{
			Console.WriteLine(text);
		}

        public Post()
        {
            Console.WriteLine("New Post");
        }
	}
}