# 🗺️ LSE Commute Explorer 📍
The project began with an intriguing proposition posted by our professor on Slack. Using data from the TFL API, we were to investigate the timeliness of buses around the London School of Economics, focusing on the stops that serve our community most closely.

After navigating to the TFL’s official website, we faced our first challenge – acquiring the API key. The process was not straightforward, sparking discussions in forums and among peers. Eventually, we discovered that subscription options varied, influencing key accessibility.

With the key in hand, we wrote Python scripts targeting the IDs of three local bus stations. Yet, this task was not as straightforward as we had hoped; inconsistencies in ID labelling between different API endpoints led us to encounter a series of bad requests.

Overcoming these initial obstacles, we successfully gathered data. However, the complexity of its structure presented a new challenge. Despite our efforts to crack the JSON formatting, the data was still perplexing, and to our dismay, we found it incomplete. Routes were missing, and the data lacked the comprehensiveness needed for a proper analysis.

Determined to press on, we contemplated a change of course. We decided to utilize the Google Maps API, which, while more straightforward and structured, came with its own limitations – the foremost being cost.

As we prepared our presentation, the complexity of our task became fully apparent. We spent nights troubleshooting empty data returns, only to learn from the TFL forum that some buses do not operate at night – a simple explanation that eluded us during our nocturnal analyses.


