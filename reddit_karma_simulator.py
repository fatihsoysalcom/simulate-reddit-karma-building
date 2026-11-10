import random

def simulate_reddit_karma_building():
    """
    Simulates a new Reddit user's journey to build karma.
    Demonstrates how post and comment interactions contribute to karma.
    """
    print("--- Reddit Karma Building Simulator ---")
    print("Starting as a new user with initial karma.")

    # As per the article, new users often start with very low karma (e.g., 1)
    post_karma = 1
    comment_karma = 1
    total_karma = post_karma + comment_karma

    print(f"\nInitial Karma: Post={post_karma}, Comment={comment_karma}, Total={total_karma}")
    print("-" * 30)

    # Simulate a series of interactions
    num_interactions = 15 # Number of posts/comments the user makes

    for i in range(1, num_interactions + 1):
        interaction_type = random.choice(["post", "comment"])
        # Simulate getting votes for this interaction.
        # A new user might get a mix of upvotes and downvotes, or just a few votes.
        # Let's make it slightly biased towards positive for demonstration,
        # but still show the impact of downvotes.
        net_votes = random.randint(-3, 7) # Can get between -3 and +7 net votes for an interaction

        print(f"\nInteraction {i}: Made a {interaction_type}.")

        if net_votes > 0:
            print(f"  Received {net_votes} net upvotes.")
            if interaction_type == "post":
                post_karma += net_votes # Upvotes increase post karma
            else:
                comment_karma += net_votes # Upvotes increase comment karma
        elif net_votes < 0:
            print(f"  Received {-net_votes} net downvotes.")
            # Downvotes decrease karma. In Reddit, individual karma types usually don't go negative.
            # We ensure karma doesn't drop below 1 for this simulation.
            if interaction_type == "post":
                post_karma = max(1, post_karma + net_votes)
            else:
                comment_karma = max(1, comment_karma + net_votes)
        else:
            print("  Received no net votes (0 upvotes/downvotes).")
        
        total_karma = post_karma + comment_karma
        print(f"  Current Karma: Post={post_karma}, Comment={comment_karma}, Total={total_karma}")
        
        # Highlight the "stuck at 1" scenario or progress
        if total_karma <= 1 and i > 1:
            print("  (Still stuck at 1 total karma! Need more positive interactions.)")
        elif total_karma > 1 and i > 1 and i < num_interactions:
            print("  (Building trust! Karma is increasing.)")

    print("\n" + "=" * 40)
    print("Simulation End.")
    print(f"Final Karma: Post={post_karma}, Comment={comment_karma}, Total={total_karma}")

    if total_karma > 10: # Arbitrary threshold to show success in building karma
        print("\nCongratulations! You've successfully built some karma and trust on Reddit.")
    else:
        print("\nKarma is still low. More consistent positive contributions are needed to build trust.")
    print("=" * 40)

if __name__ == "__main__":
    simulate_reddit_karma_building()
