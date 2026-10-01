import streamlit as st

## Fully AI Generated code used as a demo to see streamlits capabilties.

st.set_page_config(page_title="ML Project Showcase", page_icon="🧪", layout="wide")

st.markdown("""
<style>
.stApp { background: #f5f7fb; }
.hero { padding: 2.5rem; border-radius: 20px; color: white;
		background: linear-gradient(120deg,#172554,#4338ca,#7c3aed); }
.hero h1 { margin-bottom: .35rem; font-size: 2.6rem; }
.hero p { color: #e0e7ff; max-width: 760px; font-size: 1.05rem; }
.eyebrow { color: #c7d2fe; text-transform: uppercase; letter-spacing: .14em; font-size: .75rem; font-weight: 700; }
.card { background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 1.25rem; min-height: 145px; }
.card h3 { color: #1e293b; margin-top: 0; }
.muted { color: #64748b; }
.tag { display:inline-block; background:#eef2ff; color:#4338ca; border-radius:99px; padding:.25rem .6rem; margin:.15rem; font-size:.8rem; }
</style>
<div class="hero">
  <div class="eyebrow">Machine learning · Project directory</div>
  <h1>Explore the work behind the models</h1>
  <p>A home for project stories, experiments, evaluation plans, and the people behind the work. This is a showcase template; no model is included.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
nav = st.columns([1, 1, 1, 5])
for col, label in zip(nav[:3], ["Overview", "Experiments", "Documentation"]):
	col.button(label, use_container_width=True)

st.subheader("Showcase overview")
st.caption("Discover project goals, datasets, evaluation plans, and team updates in one place.")
metrics = st.columns(4)
for col, number, label in zip(metrics, ["03", "12", "08", "04"], ["Project areas", "Logged experiments", "Evaluation metrics", "Contributors"]):
	col.metric(label, number)

st.markdown("### Featured project")
left, right = st.columns([1.5, 1])
with left:
	st.markdown("""
	<div class="card">
	  <div class="eyebrow" style="color:#6366f1">Featured · In exploration</div>
	  <h3>Project Atlas</h3>
	  <p class="muted">A workspace for investigating a well-defined prediction task. Add the project's purpose, context, and progress here.</p>
	  <span class="tag">Tabular data</span><span class="tag">Responsible AI</span><span class="tag">Research</span>
	</div>""", unsafe_allow_html=True)
with right:
	st.markdown("""
	<div class="card"><h3>Project at a glance</h3>
	  <p><b>Objective</b><br><span class="muted">What question does the project aim to answer?</span></p>
	  <p><b>Current phase</b><br><span class="muted">Problem framing and data review</span></p>
	  <p><b>Owner</b><br><span class="muted">Team or contributor name</span></p>
	</div>""", unsafe_allow_html=True)

st.markdown("### Browse project areas")
areas = st.columns(3)
for col, title, description in zip(areas,
	["Data & preparation", "Experiments", "Evaluation & impact"],
	["Document sources, schema, quality checks, and preparation decisions.",
	 "Record hypotheses, configurations, and observations in a clear format.",
	 "Explain criteria, limitations, intended use, and potential risks."]):
	with col:
		st.markdown(f'<div class="card"><h3>{title}</h3><p class="muted">{description}</p></div>', unsafe_allow_html=True)

st.markdown("### Latest activity")
st.dataframe([
	{"Date": "Today", "Update": "Project workspace created", "Area": "Overview", "Status": "Ready for notes"},
	{"Date": "—", "Update": "Add an experiment summary", "Area": "Experiments", "Status": "Not started"},
	{"Date": "—", "Update": "Record evaluation criteria", "Area": "Evaluation", "Status": "Not started"},
], hide_index=True, use_container_width=True)

with st.expander("Responsible use checklist"):
	st.markdown("- State intended use and audiences clearly.\n- Note data provenance, permissions, and known gaps.\n- Select evaluation criteria that reflect real-world needs.\n- Record limitations, potential harms, and review plans.")

st.divider()
st.caption("ML Studio · Project showcase template · Add project details before sharing")
