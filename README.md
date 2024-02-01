# 🗺️ LSE Commute Explorer 📍
The project began with an intriguing proposition posted by our professor on Slack. Using data from the TFL API, we were to investigate the timeliness of buses around the London School of Economics, focusing on the stops that serve our community most closely.

After navigating to the TFL’s official website, we faced our first challenge – acquiring the API key. The process was not straightforward, sparking discussions in forums and among peers. Eventually, we discovered that subscription options varied, influencing key accessibility.

With the key in hand, we wrote Python scripts targeting the IDs of three local bus stations. Yet, this task was not as straightforward as we had hoped; inconsistencies in ID labelling between different API endpoints led us to encounter a series of bad requests.

Overcoming these initial obstacles, we successfully gathered data. However, the complexity of its structure presented a new challenge. Despite our efforts to crack the JSON formatting, the data was still perplexing, and to our dismay, we found it incomplete. Routes were missing, and the data lacked the comprehensiveness needed for a proper analysis.

Determined to press on, we contemplated a change of course. We decided to utilize the Google Maps API, which, while more straightforward and structured, came with its own limitations – the foremost being cost.

As we prepared our presentation, the complexity of our task became fully apparent. We spent nights troubleshooting empty data returns, only to learn from the TFL forum that some buses do not operate at night – a simple explanation that eluded us during our nocturnal analyses.
![Reply Image](/reply.png)

Our work on GitHub was another learning curve, filled with its own set of challenges. A hasty push sugguested by ChatGPT led to our API key being exposed, a mistake that taught us a valuable lesson in careful repository management.

Shifting our focus, we began examining alternative modes of transport from 14 LSE-affiliated dormitories to campus. We crafted a visual representation of this data on a map, with varying colour depths to signify the duration of each travel mode. Integrating this data into our visual tools proved demanding, as we navigated the intricacies of Google’s API and the JSONL file format.
![Map Image](/coloured_map.png)

The process of us setting GitHub Actions for your project is in brief like this:

• Create a Workflow File: In our GitHub repo, we first created a .github/workflows directory and within this directory, we created a YAML file to define our workflow.

• Define Workflow Events: At the start of our YAML file, we specify when the action should run. For us it’s very one hour (this could also be on a push, a pull request, or a merge).

• Define Jobs: We Set up the jobs that the action will execute, deploying our application.

• Define Steps: Within each job, we defined the steps to be taken, such as checking out our repository or executing the script.

• Include Actions: Use pre-built actions or create custom ones as needed for our steps.

• Commit and Push: Once our workflow file is configured, we committed and pushed it to our repository. GitHub will then recognize the workflow file and run the action based on the events we specified.

• MOST importantly secrets such as API keys should be stored in GitHub Secrets, not in your workflow file, to keep them secure.

After two weeks of data collection, we reached the limits of our free API credits. We consolidated our findings, analysing the data through various visualizations including box plots, line graphs and heat maps.
![Linegraph Image](/linegraph.png)
![Boxplot1 Image](/boxplot1.png)
![Boxplot2 Image](/boxplot2.png)
![CO2 Image](/CO2_heatmap.png)
[The graphics above could be found in NB04_Interactive_maps.ipynb]

Our team’s spirit was truly supportive; every member had a defined role, reflected in the meticulous notes and issues tracked in our GitHub repository.

Xinyi diligently combed through YouTube, amassing knowledge to refine our visualizations, while Vivian orchestrated our discussions, ensuring we had a physical space for collaboration. Despite the setback of inadvertently committing our API key, we chose not to dwell on blame but to focus on solutions, reinforcing our bond as a team.

Jessie, even while away in Berlin, contributed via mobile, epitomizing our remote teamwork. Vivian and Xinyi, too, lent their expertise from afar, tweaking our presentation and manuscripts.

We owe a debt of gratitude to Mr. Mustafa Can Ozkan, whose drop-in sessions were pivotal, especially for the interactive maps that became a cornerstone of our analysis. Our Professor Dr. Jon Cardoso-Silva consistently provided fresh perspectives that broke through our creative blockades, offering solutions that were both incisive and practical.

Our teacher Mr. Alexander Soldatkin was a beacon of guidance, always reminding us of our timeline and pushing us ahead of schedule. His brilliance shone brightest when he patiently fixed a critical bug on Christmas Eve, a testament to his unwavering dedication.

This is the essence of our story — a tale of unity, perseverance, and the collective pursuit of knowledge. It’s about embracing challenges, learning from our oversights, and above all, celebrating the spirit of collaboration that defines our LSE experience.
